# Play: Elder - setup

- hosts: loadbalancers
  become: true
  vars:
    app_name: "elder_app"
    retry_count: 3

  tasks:
    - name: Ensure lima-task-1 is present
      ansible.builtin.file:
        path: /opt/elder/lima-task-1
        state: directory

    - name: Template lima-task-1 config
      ansible.builtin.template:
        src: templates/lima-task-1.j2
        dest: /etc/elder/lima-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure apple-task-2 is present
      ansible.builtin.file:
        path: /opt/elder/apple-task-2
        state: directory

    - name: Template apple-task-2 config
      ansible.builtin.template:
        src: templates/apple-task-2.j2
        dest: /etc/elder/apple-task-2.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart elder service
      ansible.builtin.service:
        name: elder
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:44Z
