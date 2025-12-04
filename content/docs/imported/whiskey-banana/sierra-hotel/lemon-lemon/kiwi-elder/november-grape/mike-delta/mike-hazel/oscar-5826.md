# Play: Oscar - setup

- hosts: loadbalancers
  become: true
  vars:
    app_name: "oscar_app"
    retry_count: 3

  tasks:
    - name: Ensure papa-task-1 is present
      ansible.builtin.file:
        path: /opt/oscar/papa-task-1
        state: directory

    - name: Template papa-task-1 config
      ansible.builtin.template:
        src: templates/papa-task-1.j2
        dest: /etc/oscar/papa-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure iris-task-2 is present
      ansible.builtin.file:
        path: /opt/oscar/iris-task-2
        state: directory

    - name: Template iris-task-2 config
      ansible.builtin.template:
        src: templates/iris-task-2.j2
        dest: /etc/oscar/iris-task-2.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

  handlers:
    - name: restart oscar service
      ansible.builtin.service:
        name: oscar
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

***
Generated: 2025-11-07T18:27:44Z
