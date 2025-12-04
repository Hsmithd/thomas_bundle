# Play: Charlie - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "charlie_app"
    retry_count: 5

  tasks:
    - name: Ensure kiwi-task-1 is present
      ansible.builtin.file:
        path: /opt/charlie/kiwi-task-1
        state: directory

    - name: Template kiwi-task-1 config
      ansible.builtin.template:
        src: templates/kiwi-task-1.j2
        dest: /etc/charlie/kiwi-task-1.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure tango-task-2 is present
      ansible.builtin.file:
        path: /opt/charlie/tango-task-2
        state: directory

    - name: Template tango-task-2 config
      ansible.builtin.template:
        src: templates/tango-task-2.j2
        dest: /etc/charlie/tango-task-2.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart charlie service
      ansible.builtin.service:
        name: charlie
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:44Z
