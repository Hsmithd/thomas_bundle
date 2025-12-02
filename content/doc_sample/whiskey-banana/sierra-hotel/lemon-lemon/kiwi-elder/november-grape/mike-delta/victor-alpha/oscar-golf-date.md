# Play: Oscar - setup

- hosts: loadbalancers
  become: true
  vars:
    app_name: "oscar_app"
    retry_count: 3

  tasks:
    - name: Ensure tango-task-1 is present
      ansible.builtin.file:
        path: /opt/oscar/tango-task-1
        state: directory

    - name: Template tango-task-1 config
      ansible.builtin.template:
        src: templates/tango-task-1.j2
        dest: /etc/oscar/tango-task-1.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure alpha-task-2 is present
      ansible.builtin.file:
        path: /opt/oscar/alpha-task-2
        state: directory

    - name: Template alpha-task-2 config
      ansible.builtin.template:
        src: templates/alpha-task-2.j2
        dest: /etc/oscar/alpha-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure apple-task-3 is present
      ansible.builtin.file:
        path: /opt/oscar/apple-task-3
        state: directory

    - name: Template apple-task-3 config
      ansible.builtin.template:
        src: templates/apple-task-3.j2
        dest: /etc/oscar/apple-task-3.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

  handlers:
    - name: restart oscar service
      ansible.builtin.service:
        name: oscar
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:44Z
